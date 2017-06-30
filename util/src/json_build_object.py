from sqlalchemy import func, JSON
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement


class JsonBuildObject(FunctionElement):
    name = 'json_build_object'
    type = JSON

@compiles(JsonBuildObject, 'mysql')
def compile(element, compiler, **kw):
    """Emulate PostgreSQL json_build_object function on MySQL"""
    return "cast(json_object(%s) as json)" % compiler.process(element.clauses)

@compiles(JsonBuildObject, 'postgresql')
def compile(element, compiler, **kw):
    """Direct call to PostgreSQL json_build_object function"""
    return "json_build_object(%s)" % compiler.process(element.clauses)

func.json_build_object = JsonBuildObject
