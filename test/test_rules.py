import os

def test_rules_file():
    path = "rules/test-rule.conf"
    assert os.path.exists(path), f"Missing rule file at {path}"
    with open(path) as f:
        contents = f.read()
        assert "id:999999" in contents, "Test rule ID not found in file"

if __name__ == "__main__":
    test_rules_file()
    print("✅ Rule test passed")
