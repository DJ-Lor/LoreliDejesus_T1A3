from helper_files.helper import id_generate

# Tests that the unique identifier generated is the correct type
def test_id_generate():
    assert type(id_generate()) == int
