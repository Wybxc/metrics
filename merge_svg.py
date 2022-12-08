import sys

from lxml import etree

if __name__ == "__main__":
    # Usage: python merge_svg.py <file1> <file2> > <output_file>
    _, file1, file2, *_ = sys.argv

    svg1 = etree.parse(file1).getroot()
    svg2 = etree.parse(file2).getroot()

    # <svg width="495" height="390" viewBox="0 0 495 390" fill="none" xmlns="http://www.w3.org/2000/svg" aria-labelledby="descId">
    new_svg = etree.Element("svg")
    new_svg.set("xmlns", "http://www.w3.org/2000/svg")
    new_svg.set("aria-labelledby", "descId")
    new_svg.set("width", "495")
    new_svg.set("height", "390")
    new_svg.set("viewBox", "0 0 495 390")
    new_svg.set("fill", "none")

    svg1.set("y", "0")
    new_svg.append(svg1)

    svg2.set("y", "195")
    new_svg.append(svg2)

    sys.stdout.write(etree.tostring(new_svg, pretty_print=True).decode("utf-8"))
