def test_tmp_path(tmp_path):
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Hello, World!")
    assert temp_file.read_text() == "Hello, World!"


def test_capsys(capsys):
    print("This is pytest!")
    captured = capsys.readouterr()
    assert "pytest" in captured.out


def test_request_fixture(request):
    assert request.node.name == "test_request_fixture"