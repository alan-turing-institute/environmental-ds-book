#!/usr/bin/env python3
import sys
import json
import urllib.request
import yaml
import concurrent.futures
import traceback
import argparse

from unist import *

LAYOUT_STYLE = {
    "display": "inline-block",
    "borderRadius": 8,
    "color": "white",
    "padding": 5,
    "margin": 5,
    "textAlign": "center",
    "fontSize": 14,
}

DEFAULT_STYLE = {"background": "#4E66F6", **LAYOUT_STYLE}

styles = {
    "domains": {"background": "#579aca", **LAYOUT_STYLE},
    "type": {"background": "#8045e5", **LAYOUT_STYLE},
    "issue": {"background": "#e4640d", **LAYOUT_STYLE},
    "language": {"background": "#276be9", **LAYOUT_STYLE},
}


def fetch_yaml(url: str):
    print(f"Fetching {url}", file=sys.stderr, flush=True)
    with urllib.request.urlopen(url) as response:
        body = response.read().decode()
    return yaml.load(body, yaml.SafeLoader)


def render_notebook(name: str):
    try:
        print(f"Rendering {name}", file=sys.stderr, flush=True)
        raw_base_url = (
            f"https://raw.githubusercontent.com/eds-book/{name}/main"
        )
        config_url = f"{raw_base_url}/myst.yml"
        book_url = f"https://eds-book.github.io/{name}"

        # Load JB data
        config = fetch_yaml(config_url)
        title = config["project"]["short_title"]

        # Fetch gallery metadata
        gallery_url = f"{raw_base_url}/_gallery_info.yml"
        gallery_data = fetch_yaml(gallery_url)
        image_name = gallery_data["thumbnail"]
        image_url = f"{raw_base_url}/{image_name}"

        # Build tags
        tags = gallery_data["tags"]

        return {
            "type": "card",
            "url": book_url,
            "children": [
                {"type": "cardTitle", "children": [text(title)]},
                div(
                    [
                        div(
                            [
                                image(image_url),
                                div(
                                    [
                                        span(
                                            [text(item)],
                                            style=styles.get(name, DEFAULT_STYLE),
                                        )
                                        for name, items in tags.items()
                                        if items is not None
                                        for item in items
                                    ]
                                ),
                            ],
                            style={"textAlign": "center"},
                        )
                    ]
                )
            ],
        }
    except Exception as err:
        print(f"\n\nError rendering {name}", file=sys.stderr)
        traceback.print_exception(err, file=sys.stderr)
        return None


def render_notebooks(pool):
    with open("../src/notebook_gallery.txt") as f:
        body = f.read()

    return [c for c in pool.map(render_notebook, body.splitlines()) if c is not None]


def run_directive(name, data):
    assert name == "edsbook-notebooks"
    return [{"type": "edsbook-notebooks", "children": []}]


def run_transform(name, data):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        # Find our notebook nodes in the AST
        notebook_nodes = find_all_by_type(data, "edsbook-notebooks")

        # In-place mutate the AST to replace notebook nodes with card grids
        children = render_notebooks(pool)

        # Mutate our notebook nodes in-place
        for node in notebook_nodes:
            node.clear()
            node.update(grid([1, 1, 2, 3], children))
            node["children"] = children

    return data


edsbookGalleryDirective = {
    "name": "edsbook-notebooks",
    "doc": "An example directive for embedding a EDS Book notebook gallery.",
}
edsbookGalleryTransform = {
    "stage": "document",
}

PLUGIN_SPEC = {
    "name": "EDS Book Gallery",
    "directives": [edsbookGalleryDirective],
    "transforms": [edsbookGalleryTransform],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        data = json.load(sys.stdin)
        json.dump(run_directive(args.directive, data), sys.stdout)
    elif args.transform:
        data = json.load(sys.stdin)
        json.dump(run_transform(args.transform, data), sys.stdout)
    elif args.role:
        raise NotImplementedError
    else:
        json.dump(PLUGIN_SPEC, sys.stdout)