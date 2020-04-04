import xml.etree.ElementTree as ET
import csv


def parse_xml_2csv(root):
    with open('city_latitude.csv', 'w', encoding="utf-8") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['City', 'PointX','PointY'])
        for elem in root.iter("Record"):
            for subelem in elem.iter("Values"):
                point_x = subelem[1][0].text
                point_y = subelem[1][1].text
                city_name= subelem[4].text
            filewriter.writerow([city_name, point_x, point_y])


def fetch_xml():
    tree = ET.parse('CITY.xml')
    root = tree.getroot()
    return root


if __name__ == '__main__':
    root_tree = fetch_xml()
    parse_xml_2csv(root_tree)

