from sqlalchemy import func, String
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement


class GroupConcat(FunctionElement):
    name = 'group_concat'
    type = String


@compiles(GroupConcat, 'mysql')
def compile(element, compiler, **kw):
    """Direct call to MySQL group_concat function"""
    return "group_concat(%s)" % compiler.process(element.clauses)


@compiles(GroupConcat, 'postgresql')
def compile(element, compiler, **kw):
    """Emulate MySQL group_concat function on PostgreSQL"""
    return "string_agg(%s, ',')" % compiler.process(element.clauses)


func.group_concat = GroupConcat
