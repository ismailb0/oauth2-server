from sqlalchemy import func, JSON
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement


class JsonAgg(FunctionElement):
    name = 'json_agg'
    type = JSON

@compiles(JsonAgg, 'mysql')
def compile(element, compiler, **kw):
    """Emulate PostgreSQL json_agg function on MySQL"""
    return "cast(concat('[', group_concat(json_quote(%s)), ']') as json)" % compiler.process(element.clauses)

@compiles(JsonAgg, 'postgresql')
def compile(element, compiler, **kw):
    """Direct call to PostgreSQL json_agg function"""
    return "json_agg(%s)" % compiler.process(element.clauses)

func.json_agg = JsonAgg
