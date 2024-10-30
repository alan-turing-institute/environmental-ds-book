"""uuid.py: Thin wrapper around python uuid (universally unique identifier) module."""
##source: https://github.com/bp/resqpy/blob/13061fee94c69a466863cab048bfdba70d414f36/resqpy/olio/uuid.py

# NB: at present the code does not enforce multiprocessor safe generation of unique identifiers
# it calls uuid.uuid1() to generate new uuids, ie. using version 1 of the iso standard options

import uuid

test_mode = False
test_latest_int = 0

max_version_string_length = 10


def new_uuid():
    """Returns a new uuid based on the time (to 100ns) & MAC address option of the iso standard.

    returns:
       uuid.UUID object

    notes:
       at present, the multi-processor safe functionality is not deployed, so multiple processors
       sharing the same MAC address could generate the same uuid simultaneously;
       an integer sequence is generated when in test mode
    """

    global test_latest_int
    if test_mode:
        test_latest_int += 1
        return uuid.UUID(bytes=test_latest_int.to_bytes(16, byteorder='big'))
    else:
        return uuid.uuid4()  # time to 100ns & MAC address


def uuid_from_string(uuid_str):
    """Returns a uuid object for the given uuid string; hyphens are ignored.

    arguments:
       uuid_str (string): the hexadecimal representation of the 128 bit uuid integer;
          hyphens are ignored

    returns:
       uuid.UUID object

    notes:
       if a uuid.UUID object is passed by accident, it is returned;
       if the string starts with an underscore, the underscore is skipped (to cater for a fesapi quirk);
       any tail beyond the uuid string is ignored
    """

    if uuid_str is None:
        return None
    if isinstance(uuid_str, uuid.UUID):
        return uuid_str  # resilience to accidentally passing a uuid object
    if isinstance(uuid_str, int):
        return uuid_from_int(uuid_str)
    try:
        if uuid_str[0] == '_':  # tolerate one of the fesapi quirks
            if len(uuid_str) < 37:
                return None
            return uuid.UUID(uuid_str[1:37])
        else:
            if len(uuid_str) < 36:
                return None
            return uuid.UUID(uuid_str[:36])
    except Exception:
        # could log or raise an error or warning?
        return None


def uuid_from_int(uuid_int):
    """Returns a uuid object for the given uuid int."""
    return None if uuid_int is None else uuid.UUID(int=uuid_int)


def uuid_as_bytes(uuid_obj):
    """Returns the uuid as a 16 byte bytes sequence; same as uuid_obj.bytes.

    arguments:
       uuid_obj (uuid.UUID object): the uuid for which a bytes representation is required

    returns:
       bytes (16 bytes long)
    """

    if uuid_obj is None:
        return None
    if isinstance(uuid_obj, int):
        uuid_obj = uuid_from_int(uuid_obj)
    elif isinstance(uuid_obj, str):
        uuid_obj = uuid_from_string(uuid_obj)  # resilience to accidental string arg
    assert isinstance(uuid_obj, uuid.UUID)
    return uuid_obj.bytes


def uuid_as_int(uuid_obj):
    """Returns the uuid as a 128 bit int; same as uuid_obj.int.

    arguments:
       uuid_obj (uuid.UUID object): the uuid for which a bytes representation is required

    returns:
       int (128 bit, though python no longer differentiates int precision)
    """

    if uuid_obj is None:
        return None
    if isinstance(uuid_obj, int):
        return uuid_obj
    if isinstance(uuid_obj, str):
        uuid_obj = uuid_from_string(uuid_obj)  # resilience to accidental string arg
    if not isinstance(uuid_obj, uuid.UUID):
        raise ValueError(f'non uuid object where uuid expected: {uuid_obj}; type: {type(uuid_obj)}')
    return uuid_obj.int


def matching_uuids(uuid_a, uuid_b):
    """Returns True if the 2 uuid objects are for the same id; False otherwise.

    arguments:
       uuid_a, uuid_b (uuid.UUID objects): the two uuids to be compared

    returns:
       boolean: True if the two uuids are the same; False otherwise

    note:
       this function is resilient to uuids being passed in hexadecimal string format, or int
    """

    if isinstance(uuid_a, str):
        uuid_a = uuid_from_string(uuid_a)  # resilience to accidental string arg
    if isinstance(uuid_b, str):
        uuid_b = uuid_from_string(uuid_b)
    if uuid_a is None or uuid_b is None:
        return False
    if not isinstance(uuid_a, int):
        uuid_a = uuid_a.int
    if not isinstance(uuid_b, int):
        uuid_b = uuid_b.int
    return uuid_a == uuid_b


def uuid_in_list(uuid, uuid_list):
    """Returns True if the uuid is in the list of uuids."""
    for uuid_b in uuid_list:
        if matching_uuids(uuid, uuid_b):
            return True
    return False


def version_string(uuid_obj):
    """Returns an integer string rendering of the time element of the uuid.

    arguments:
       uuid_obj (uuid.UUID): the uuid for which a string representation of the time component is required

    returns:
       string (of digits)

    notes:
       this function has nothing to do with the uuid.version attribute, it is used to populate the version
       field of a resqml citation block;
       the time component of the uuid is the number of 100ns periods that have elapsed since October 1582
       (when the Gregorian calendar was adopted), as a 60 bit integer
    """

    if isinstance(uuid_obj, str):
        uuid_obj = uuid_from_string(uuid_obj)  # resilience to accidental string arg
    v_str = str(uuid_obj.time)
    if len(v_str) > max_version_string_length:
        v_str = v_str[:max_version_string_length]
    return v_str


def is_uuid(uuid_obj):
    """Returns boolean indicating whether uuid_obj seems to be a uuid, in any allowed form."""

    if isinstance(uuid_obj, uuid.UUID):
        return True
    if isinstance(uuid_obj, int):
        try:
            _ = uuid_from_int(uuid_obj)
            return True
        except Exception:
            return False
    if not uuid_obj or not isinstance(uuid_obj, str):
        return False
    if uuid_obj[0] == '_':
        return len(uuid_obj) == 37
    return len(uuid_obj) == 36
    # could also check for hyphens in correct places, and hexadecimals only


def gen_new_uuid_edsbook():
    while True:
        id_ = new_uuid()
        if not uuid_in_list(id_, existing_uuid):
            break
    print(id_)


existing_uuid = ['39d9c177-11da-41b2-9b64-63f4c1c834b3', '93463cac-471a-469d-ad52-0514fd9b67f2',
                 '3286b92f-4fae-4cc6-a29e-e408bc844542', 'b128b282-dee7-44a7-bc21-f1fd21452a83',
                 '435f534c-e49b-43c3-9bd6-3393100bef3f', 'ea34568e-d86e-4720-be2f-3f826f66a26c',
                 'ac327c3a-5264-40a2-8c6e-1e8d7c4b37ef', '94486a7f-e046-461f-bbb9-334ec7b57040',
                 'bc30df18-fce2-42fa-aade-1ce5b7f3ca3c', '15d986da-2d7c-44fb-af71-700494485def',
                 'a2875cdc-ba6a-49dc-aab7-cdf7c4fc0fa8', '1b8921af-e77f-4ccf-ae38-4813cdceba0f',
                 'b34facfa-cea8-48f5-89f6-f11ce00812a9', '93463cac-471a-469d-ad52-0514fd9b67f2',
                 '67a1e320-7c47-4ea9-8df8-e868326bc90b']

gen_new_uuid_edsbook()
