base_conversion = {
    "name": "base_conversion",
    "units": [
        {
            "name": "b2",
            "_internal_accepted_names": ["b2"],
            "si": "b2",
            "_internal_conversion": {
                "b3": lambda n: n * 10 ** 5,  # n to dyn
                "b4": lambda n: n * 7.23301,  # n to pdl
                "b5": lambda n: n * 0.10197,  # n to kp
            },  
        },
                {
            "name": "b3",
            "_internal_accepted_names": ["b3"],
            "si": "b3", 
            "_internal_conversion": {
                "b2": lambda n: n * 10 ** 5,  # n to dyn
                "b4": lambda n: n * 7.23301,  # n to pdl
                "b5": lambda n: n * 0.10197,  # n to kp
            },    
        },
                {
            "name": "b4",
            "_internal_accepted_names": ["b4"],
            "si": "b4",   
        },
                {
            "name": "b5",
            "_internal_accepted_names": ["b5"],
            "si": "b5",   
        },
                {
            "name": "b6",
            "_internal_accepted_names": ["b6"],
            "si": "b6",   
        },
                {
            "name": "b7",
            "_internal_accepted_names": ["b7"],
            "si": "b7",   
        },
                {
            "name": "b8",
            "_internal_accepted_names": ["b8"],
            "si": "b8",   
        },
                {
            "name": "b9",
            "_internal_accepted_names": ["b9"],
            "si": "b9",   
        },
                {
            "name": "b10",
            "_internal_accepted_names": ["b10"],
            "si": "b10",   
        },
    
    ]
}