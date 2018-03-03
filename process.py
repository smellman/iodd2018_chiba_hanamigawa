# encoding: utf-8
import csv
import json

start_year = 2012
end_year = 2017
file_path = '../../process/'

def parseInt(value):
    if value != '':
        return int(value)
    else:
        return 0

mapping = {
    "総数": "",
    "朝日ケ丘１丁目": "12102001101",
    "朝日ケ丘２丁目": "12102001102",
    "朝日ケ丘３丁目": "12102001103",
    "朝日ケ丘４丁目": "12102001104",
    "朝日ケ丘５丁目": "12102001105",
    "朝日ケ丘町": "121020012",
    "天戸町": "121020020",
    "内山町": "121020030",
    "み春野１丁目": "12102004101",
    "み春野２丁目": "12102004102",
    "み春野３丁目": "12102004103",
    "宇那谷町": "121020042",
    "柏井１丁目": "121020051",
    "柏井４丁目": "121020052",
    "柏井町": "121020053",
    "検見川町１丁目": "12102006001",
    "検見川町２丁目": "12102006002",
    "検見川町３丁目": "12102006003",
    "検見川町５丁目": "12102006004",
    "こてはし台１丁目": "12102007001",
    "こてはし台２丁目": "12102007002",
    "こてはし台３丁目": "12102007003",
    "こてはし台４丁目": "12102007004",
    "こてはし台５丁目": "12102007005",
    "こてはし台６丁目": "12102007006",
    "犢橋町": "121020080",
    "作新台１丁目": "12102010001",
    "作新台２丁目": "12102010002",
    "作新台３丁目": "12102010003",
    "作新台４丁目": "12102010004",
    "作新台５丁目": "12102010005",
    "作新台６丁目": "12102010006",
    "作新台７丁目": "12102010007",
    "作新台８丁目": "12102010008",
    "さつきが丘１丁目": "12102011001",
    "さつきが丘２丁目": "12102011002",
    "三角町": "121020120",
    "武石町１丁目": "12102013001",
    "武石町２丁目": "12102013002",
    "大日町": "121020140",
    "千種町": "121020150",
    "長作台１丁目": "12102016101",
    "長作台２丁目": "12102016102",
    "長作町": "121020162",
    "浪花町": "121020170",
    "西小中台": "121020180",
    "畑町": "121020190",
    "花島町": "121020200",
    "花園１丁目": "12102021001",
    "花園２丁目": "12102021002",
    "花園３丁目": "12102021003",
    "花園４丁目": "12102021004",
    "花園５丁目": "12102021005",
    "花園町": "121020220",
    "花見川１": "12102023001",
    "花見川２": "12102023002",
    "花見川３": "12102023003",
    "花見川４": "12102023004",
    "花見川５": "12102023005",
    "花見川６": "12102023006",
    "花見川７": "12102023007",
    "花見川８": "12102023008",
    "花見川９": "12102023009",
    "幕張町１丁目": "12102024001",
    "幕張町２丁目": "12102024002",
    "幕張町３丁目": "12102024003",
    "幕張町４丁目": "12102024004",
    "幕張町５丁目": "12102024005",
    "幕張町６丁目": "12102024006",
    "幕張本郷１丁目": "12102025001",
    "幕張本郷２丁目": "12102025002",
    "幕張本郷３丁目": "12102025003",
    "幕張本郷４丁目": "12102025004",
    "幕張本郷５丁目": "12102025005",
    "幕張本郷６丁目": "12102025006",
    "幕張本郷７丁目": "12102025007",
    "南花園１丁目": "12102026001",
    "南花園２丁目": "12102026002",
    "宮野木台１丁目": "12102027001",
    "宮野木台２丁目": "12102027002",
    "宮野木台３丁目": "12102027003",
    "宮野木台４丁目": "12102027004",
    "横戸台": "121020280",
    "横戸町": "121020290",
    "瑞穂１丁目": "12102030001",
    "瑞穂２丁目": "12102030002",
    "瑞穂３丁目": "12102030003"
}

def parse():
    output = {}
    for _year in range(start_year, end_year + 1):
        year = str(_year)
        process_file = file_path + year + ".csv"
        with open(process_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            count = 0
            area = ""
            for row in reader:
                count = count + 1
                if count <= 3:
                    continue
                _area = row[0].strip()
                if _area != "" and area != _area:
                    area = _area
                if area == "花見川":
                    continue
                if area == "花見川５":
                    continue
                if area == "朝日ヶ丘町":
                    continue
                if not area in output:
                    output[area] = {}
                    if area in mapping:
                        output[area]["KEY_CODE"] = mapping[area]
                if not year in output[area]:
                    output[area][year] = {}
                target = row[1].strip()
                count_all = parseInt(row[2])
                count_young = parseInt(row[3])
                count_middle = parseInt(row[4])
                count_old = parseInt(row[5])
                output[area][year][target] = {
                    "count_all": count_all,
                    "count_young": count_young,
                    "count_middle": count_middle,
                    "count_old": count_old
                }
    return output

def parse_by_year():
    for _year in range(start_year, end_year + 1):
        output = {}
        year = str(_year)
        process_file = file_path + year + ".csv"
        with open(process_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            count = 0
            area = ""
            for row in reader:
                count = count + 1
                if count <= 3:
                    continue
                _area = row[0].strip()
                if _area != "" and area != _area:
                    area = _area
                if area == "花見川":
                    continue
                if area == "花見川５":
                    continue
                if area == "朝日ヶ丘町":
                    continue
                if not area in output:
                    output[area] = {}
                    if area in mapping:
                        output[area]["KEY_CODE"] = mapping[area]
                target = row[1].strip()
                count_all = parseInt(row[2])
                count_young = parseInt(row[3])
                count_middle = parseInt(row[4])
                count_old = parseInt(row[5])
                output[area][target] = {
                    "count_all": count_all,
                    "count_young": count_young,
                    "count_middle": count_middle,
                    "count_old": count_old
                }
        json.dumps(output)

def make_geojson():
    for _year in range(start_year, end_year + 1):
        f = open("hanamigawa_points.geojson")
        geojson_all = json.load(f)
        f.close()
        f = open("hanamigawa_points.geojson")
        geojson_man = json.load(f)
        f.close()
        f = open("hanamigawa_points.geojson")
        geojson_woman = json.load(f)
        f.close()
        year = str(_year)
        process_file = file_path + year + ".csv"
        with open(process_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            count = 0
            area = ""
            for row in reader:
                count = count + 1
                if count <= 3:
                    continue
                _area = row[0].strip()
                if count % 3 == 1:
                    target = geojson_all
                elif count % 3 == 2:
                    target = geojson_man
                else:
                    target = geojson_woman
                if _area != "" and area != _area:
                    area = _area
                if area == "花見川":
                    continue
                if area == "花見川５":
                    continue
                if area == "朝日ヶ丘町":
                    continue
                #if not area in output:
                #    output[area] = {}
                #    if area in mapping:
                #        output[area]["KEY_CODE"] = mapping[area]
                if not area in mapping:
                    continue
                key = mapping[area]
                #target = row[1].strip()
                count_all = parseInt(row[2])
                count_young = parseInt(row[3])
                count_middle = parseInt(row[4])
                count_old = parseInt(row[5])
                for i in range(0, len(target["features"])):
                    if str(target["features"][i]["properties"]["key"]) == key:
                        target["features"][i]["properties"] = {
                            "key": key,
                            "count_all": count_all,
                            "count_young": count_young,
                            "count_middle": count_middle,
                            "count_old": count_old
                        }
        fp = open(year + '_all_data.geojson', 'w')
        fp.write(json.dumps(geojson_all, indent=4))
        fp.close()
        fp = open(year + '_man_data.geojson', 'w')
        fp.write(json.dumps(geojson_man, indent=4))
        fp.close()
        fp = open(year + '_woman_data.geojson', 'w')
        fp.write(json.dumps(geojson_woman, indent=4))
        fp.close()


if __name__ == '__main__':
    #output = parse()
    #print(json.dumps(output))
    make_geojson()
"""
想定するハッシュ

{
    "総数": {
        "2012": {
            "総数": {
                "all": ...
            },
            "男": "....",
            "女": "...."
        },
        "2013": {
            ....
        },
        ...
    },
    "朝日ヶ丘町": {
        ...
    },
    ...
}
"""
