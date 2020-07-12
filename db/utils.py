from pathlib import Path
import subprocess
# from itertools import chain
import re
from jinja2 import Template
import fire
import urllib
import pinyin




def camel_case_split(str):
    return re.findall(r'[0-9]+|[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)


'''
it is not idempotent! just run once.
'''
def clean_file_name(a_dir):
    for path in Path(a_dir).rglob("*"):  #iterdir():
        if path.is_file():
            old_name = path.stem
            old_extension = path.suffix
            directory = path.parent
            new_name = old_name.replace('&','').replace('_','').replace('(','').replace(')','').replace('[','').replace(']','').replace(' ','').replace('-','').replace('"','').replace("'",'').replace(",","").replace('.DVDRip.480p.x264.AC3CMCT','') + old_extension  #urllib.parse.quote(old_name) + old_extension
            path.rename(Path(directory, new_name))


def split_camel_file(a_dir):
    for path in Path(a_dir).rglob("*"):  #iterdir():
        if path.is_file():
            old_name = path.stem
            old_extension = path.suffix
            directory = path.parent
            new_name = re.sub(r'^[0-9]+.', '', old_name) + old_extension  #'.'.join(camel_case_split(old_name))
            #print(old_name)
            #print(new_name)
            path.rename(Path(directory, new_name))


def chn_eng(chn_char):
    return pinyin.get(chn_char, format="strip", delimiter="")


def file_chn_eng(a_dir):
    for path in Path(a_dir).rglob("*"):  #iterdir():
        if path.is_file():
            old_name = path.stem
            old_extension = path.suffix
            directory = path.parent
            new_name = 'China.' + chn_eng(old_name) + old_extension
            #print(new_name)
            path.rename(Path(directory, new_name))


def add_prefix(a_dir):
    for path in Path(a_dir).rglob("*"):  #iterdir():
        if path.is_file():
            old_name = path.stem
            old_extension = path.suffix
            directory = path.parent
            new_name = 'China.'+ old_name + old_extension
            path.rename(Path(directory, new_name))


'''
purpose: adding a extend to a file.
input: a string of file.
output: a string of file with added extend.
'''
def update_suffix(input_str,exts):
    path_input = Path(input_str)
    if not path_input.exists():
        return None
    path_output = path_input.with_suffix(exts)
    return str(path_output)


'''
purpose: list all the files of the extend under the path
'''
def list_files(path, exts=['.mp4']):
    base_path = Path(path)
    if not base_path.exists():
        return None
    files = [p for p in base_path.rglob('*') if p.suffix in exts]
    return files


'''
purpose: convert a list of files to a list of (file, file.new-extend) to feed ffmpeg for converting.
'''
def convert_list(files, to_format):
    if not files or len(files) < 1:
        return None
    t1 = []
    for i in files:
        o1 = update_suffix(str(i), to_format)
        if o1 and not Path(o1).exists(): # ignore the file if it's converted before. 
            t1.append((str(i),o1))
    return t1


def run_ffconvert(convertlist):
    for t in convertlist:
        input_str = t[0]
        output_str = t[1]
        to_mp4_cmd_raw = f"ffmpeg -i input_str -c:v libx264 -crf 23 -profile:v baseline -level 3.0 -pix_fmt yuv420p -c:a aac -ac 2 -b:a 128k -movflags faststart output_str"
        to_mp4_cmd_list = to_mp4_cmd_raw.split()
        to_mp4_cmd_list = [w.replace('input_str', input_str) for w in to_mp4_cmd_list]
        to_mp4_cmd_list = [w.replace('output_str', output_str) for w in to_mp4_cmd_list]
        print(to_mp4_cmd_list)
        subprocess.run(to_mp4_cmd_list)


def to_mp4(from_dir="/mnt/g/ent/movies/cartoon",nlimit=6):
    # configs
    # from_dir =     
    exts = ['.mkv','.rmvb','.avi']
    to_format = '.mp4'
    files = list_files(from_dir, exts)
    t1 = convert_list(files,to_format)
    run_ffconvert(t1[:nlimit])


def find_year(input_str):
    pattern = re.compile(r'(19|20)\d\d')
    result = pattern.search(input_str)
    if not result:
        return None
    else:
        return result.group()


def find_duration():
    pass


def to_db_str(from_dir=".", exts=[".mp4"]):
    files = list_files(from_dir, exts)
    res = []
    for f in files:
        video_file = str(f).replace("'","''")
        video_name = f.stem.replace("'","''")
        video_year = find_year(video_name)
        t = Template("insert into videoshare.video (video_name, year, file_name) values ('{{video_name}}', {% if video_year %} {{video_year}}{% else %}NULL{% endif %}, '{{video_file}}');")
        one_str = t.render(video_name=video_name, video_year=video_year,video_file=video_file)
        res.append(one_str)
    return res


def files_db_sync():
    db_str = to_db_str('/mnt/g/ent/movies')
    for i in db_str:
        print(i)


if __name__ == '__main__':
    fire.Fire()
