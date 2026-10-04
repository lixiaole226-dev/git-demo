def greet(name):
    """返回对 name 的问候语。

    Args:
        name: 非空字符串
    Returns:
        问候语字符串
    Raises:
        ValueError: name 为空
    """
    if not name or not name.strip():
        raise ValueError("name 不能为空")
    return f"Hello, {name.strip()}!"