from bs4 import Tag


def get_transform_value(tag: Tag):
    if not "transform" in tag.attrs:
        return (0.0, 0.0)

    transform = tag.get("transform")
    if not transform:
        return (0.0, 0.0)

    tmpx, tmpy = transform.split(",")
    x = float(tmpx.replace("translate(", ""))
    y = float(tmpy.replace(")", ""))

    return x, y
