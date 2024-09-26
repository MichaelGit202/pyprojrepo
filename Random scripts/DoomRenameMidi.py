import os


#I know there was no other way around this but hardcoding != faster
#literally this system just corelates the def doom song name with the map number
#and adds the prefix "name" of the wad. so dumb
#also why do case statements not exist in python are you serious

def rename(name, path, b):
    split_tup = os.path.splitext(b)
    print(name)
    
    if split_tup[1] == "mus":
        split_tup[1] = "midi"

    os.rename(path + "\\" + b, path + "\\" + name + split_tup[1])
    
print('name')
name = input()
path = os.getcwd() + '\\MidiRename'
a = os.listdir(path)
num = 1
for b in a:
    split_tup = os.path.splitext(b)
    print(b.lower())
    if "d_runnin" + split_tup[1] == b.lower():
        rename(name + ' map01', path, b)
    elif  "d_runni2" + split_tup[1] == b.lower():
        rename(name + ' map15', path, b)
    elif  "d_stalks" + split_tup[1] == b.lower():
        rename(name + ' map02', path, b)
    elif  "d_stlks2" + split_tup[1] == b.lower():
        rename(name + ' map11', path, b)
    elif  "d_stlks3" + split_tup[1] == b.lower():
        rename(name + ' map17', path, b)
    elif  "d_countd" + split_tup[1] == b.lower():
        rename(name + ' map03', path, b)
    elif  "d_count2" + split_tup[1] == b.lower():
        rename(name + ' map21', path, b)
    elif  "d_betwee" + split_tup[1] == b.lower():
        rename(name + ' map04', path, b)
    elif  "d_doom" + split_tup[1] == b.lower():
        rename(name + ' map05', path, b)
    elif  "d_doom2" + split_tup[1] == b.lower():
        rename(name + ' map13', path, b)
    elif  "d_the_da" + split_tup[1] == b.lower():
        rename(name + ' map06', path, b)
    elif  "d_theda2" + split_tup[1] == b.lower():
        rename(name + ' map12', path, b)
    elif  "d_theda3" + split_tup[1] == b.lower():
        rename(name + ' map24', path, b)
    elif  "d_shawn" + split_tup[1] == b.lower():
        rename(name + ' map07', path, b)
    elif  "d_shawn2" + split_tup[1] == b.lower():
        rename(name + ' map19', path, b)
    elif  "d_shawn3" + split_tup[1] == b.lower():
        rename(name + ' map29', path, b)
    elif  "d_ddtblu" + split_tup[1] == b.lower():
        rename(name + ' map08', path, b)
    elif  "d_ddtbl2" + split_tup[1] == b.lower():
        rename(name + ' map14', path, b)
    elif  "d_ddtbl3" + split_tup[1] == b.lower():
        rename(name + ' map22', path, b)
    elif  "d_in_cit" + split_tup[1] == b.lower():
        rename(name + ' map09', path, b)
    elif  "d_dead" + split_tup[1] == b.lower():
        rename(name + ' map10', path, b)
    elif  "d_dead2" + split_tup[1] == b.lower():
        rename(name + ' map16', path, b)
    elif  "d_romero" + split_tup[1] == b.lower():
        rename(name + ' map18', path, b)
    elif  "d_romer2" + split_tup[1] == b.lower():
        rename(name + ' map27', path, b)
    elif  "d_messag" + split_tup[1] == b.lower():
        rename(name + ' map20', path, b)
    elif  "d_messg2" + split_tup[1] == b.lower():
        rename(name + ' map26', path, b)
    elif  "d_ampie" + split_tup[1] == b.lower():
        rename(name + ' map23', path, b)
    elif  "d_adrian" + split_tup[1] == b.lower():
        rename(name + ' map25', path, b)
    elif  "d_tense" + split_tup[1] == b.lower():
        rename(name + ' map28', path, b)
    elif  "d_openin" + split_tup[1] == b.lower():
        rename(name + ' map30', path, b)
    elif  "d_evil" + split_tup[1] == b.lower():
        rename(name + ' map31', path, b)
    elif  "d_ultima" + split_tup[1] == b.lower():
        rename(name + ' map32', path, b)
    elif  "d_dm2int" + split_tup[1] == b.lower():
        rename(name + ' intermission', path, b)
    elif  "d_read_m" + split_tup[1] == b.lower():
        rename(name + ' End Game Music', path, b)
    elif  "d_dm2ttl" + split_tup[1] == b.lower():
        rename(name + ' title music', path, b)
    else:
        rename(name + " map" + str(num + 32) , path, b)
        num += 1
        
