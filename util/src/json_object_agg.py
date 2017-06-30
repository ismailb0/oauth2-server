from sqlalchemy import func, JSON
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement


class JsonObjectAgg(FunctionElement):
    name = 'json_object_agg'
    type = JSON

@compiles(JsonObjectAgg, 'mysql')
def compile(element, compiler, **kw):
    """Emulate PostgreSQL json_object_agg function on MySQL"""
    key, value = map(compiler.process, element.clauses)
    result = "cast(concat('{{', group_concat(json_quote({}), ' : ', json_quote({})), '}}') as json)".format(key, value)
    return result

@compiles(JsonObjectAgg, 'postgresql')
def compile(element, compiler, **kw):
    """Direct call to PostgreSQL json_object_agg function"""
    return "json_object_agg(%s)" % compiler.process(element.clauses)

func.json_object_agg = JsonObjectAgg
