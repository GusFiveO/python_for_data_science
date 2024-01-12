def all_thing_is_obj(obj: any):
    type_dic = {list: "List",
                tuple: "Tuple",
                set: "Set",
                dict: "Dict",
                str: "String"}

    object_type = type(obj)
    type_dic_name = type_dic.get(object_type)

    if type_dic_name == "String":
        print(f"{obj} is in the kitchen : {object_type}")
    elif type_dic_name:
        print(f"{type_dic_name} : {object_type}")
    else:
        print("Type not found")
    return 42
