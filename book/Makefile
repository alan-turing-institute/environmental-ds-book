# Default target
all: book

# Install build dependencies
deps:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Build the book and build the HTML version
book:
	cd book && jupyter book build --html