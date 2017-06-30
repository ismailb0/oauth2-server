from flask.ext.restful import reqparse

from errors import InputError


def parse(arguments):
    parser = reqparse.RequestParser()
    for argument in arguments:
        # WTF: parser.add_argument(argument) returns an error
        parser.add_argument(
            argument.name,
            location=argument.location,
            type=argument.type,
            help=argument.help,
            required=argument.required,
            default=argument.default,
        )

    try:
        args = parser.parse_args()
    except Exception as e:
        raise InputError(e.data, None)

    return args
