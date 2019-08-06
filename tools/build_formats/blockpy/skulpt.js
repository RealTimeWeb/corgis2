{% set library_name = dataset.name | snake_case %}

var $builtinmodule = function(name)
{
    var mod = {};
    
    mod.get = new Sk.builtin.func(function(property, index, index_value) {
        Sk.builtin.pyCheckArgs("get", arguments, 3, 3);
        Sk.builtin.pyCheckType("property", "string", Sk.builtin.checkString(property));
        Sk.builtin.pyCheckType("index", "string", Sk.builtin.checkString(index));
        Sk.builtin.pyCheckType("index_value", "string", Sk.builtin.checkString(index_value));
        property = property.v;
        index = index.v;
        index_value = index_value.v;
        var dataset = blockpy._IMPORTED_DATASETS[{{ library_name | tojson }}];
        var data = [];
        if (index != '(None)') {
            for (var i = 0; i < dataset[property].data.length; i += 1) {
                if (dataset[index].data[i] == index_value) {
                    data.push(dataset[property].data[i]);
                }
            }
        } else {
            data = dataset[property].data;
        }
        return Sk.ffi.remapToPy(data);
    });
    
    {% for interface in interfaces %}
    mod.{{ interface.name | snake_case }} = new Sk.builtin.func(function() {
        Sk.builtin.pyCheckArgs("{{ interface.name | snake_case }}", arguments, 0, 0);
        if (!({{ library_name | tojson }} in _IMPORTED_COMPLETE_DATASETS)) {
            alert("This library has not finished loading yet. Please wait about 10 seconds and try again.")
        } else {
            return blockpy._IMPORTED_COMPLETE_DATASETS[{{ library_name | tojson }}];
        }
    });
    {% endfor %}
    
    mod._tifa_definitions = new Sk.builtin.func(function() {
        return Sk.ffi.remapToPy({"type": "ModuleType",
        "fields": {
            'get': {
                "type": "FunctionType",
                "name": 'get',
                "returns": {
                    "type": "ListType",
                    "empty": False,
                    "subtype": {"type": "NumType"}
                }
            },
            'get_{{ dataset.row | snake_case }}': {
                "type": "FunctionType",
                "name": 'get_{{ dataset.row | snake_case }}',
                "returns": {{ tifa_definitions }}
            },
        }
    });
    });

    return mod;
}