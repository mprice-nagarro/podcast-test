import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

rss = xml_tree.Element('rss', {'version': '2.0', 'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd', 'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'})
channel = xml_tree.SubElement(rss, 'channel')
link = yaml_data['link']
xml_tree.SubElement(channel, 'title').text = yaml_data['title']
xml_tree.SubElement(channel, 'format').text = yaml_data['format']
xml_tree.SubElement(channel, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel, 'description').text = yaml_data['description']
xml_tree.SubElement(channel, 'itunes:image', {'href': link+yaml_data['image']})
xml_tree.SubElement(channel, 'language').text = yaml_data['language']
xml_tree.SubElement(channel, 'link').text = link
xml_tree.SubElement(channel, 'itunes:category', {'text': yaml_data['category']})

for item in yaml_data['item']:
    xml_item = xml_tree.SubElement(channel, 'item')
    xml_tree.SubElement(xml_item, 'title').text = item['title']
    xml_tree.SubElement(xml_item, 'description').text = item['description']
    xml_tree.SubElement(xml_item, 'itunes:author').text = yaml_data['author']
    xml_tree.SubElement(xml_item, 'pubDate').text = item['published']
    xml_tree.SubElement(xml_item, 'enclosure', {'url': link+item['file'], 'length': str(item['length']), 'type': 'audio/mpeg'})
    xml_tree.SubElement(xml_item, 'itunes:duration').text = item['duration']

output = xml_tree.ElementTree(rss)
output.write('podcast.xml', encoding='utf-8', xml_declaration=True)