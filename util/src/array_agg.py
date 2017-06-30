from sqlalchemy import func, JSON
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement


class ArrayAgg(FunctionElement):
    name = 'array_agg'
    type = JSON

@compiles(ArrayAgg, 'mysql')
def compile(element, compiler, **kw):
    """Emulate PostgreSQL array_agg function on MySQL"""
    return "cast(concat('[', group_concat(ifnull(json_quote(%s), 'null')), ']') as json)" % compiler.process(element.clauses)

@compiles(ArrayAgg, 'postgresql')
def compile(element, compiler, **kw):
    """Direct call to PostgreSQL array_agg function"""
    return "array_agg(%s)" % compiler.process(element.clauses)

func.array_agg = ArrayAgg
