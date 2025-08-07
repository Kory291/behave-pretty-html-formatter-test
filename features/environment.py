from behave_html_pretty_formatter import PrettyHTMLFormatter
from behave.formatter.base import StreamOpener

def before_all(context):
    # this doesn't break anything
    if not any(isinstance(formatter, PrettyHTMLFormatter) for formatter in context._runner.formatters):
        pretty_html_formatter = PrettyHTMLFormatter(StreamOpener("first.html"), context.config)
        context._runner.formatters.append(pretty_html_formatter)

def before_feature(context, feature):
    # this breaks
    # pretty_html_formatter = PrettyHTMLFormatter(StreamOpener("second.html"), context.config)
    # context._runner.formatters.append(pretty_html_formatter)
    pass

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    pass

def after_feature(context, feature):
    # pretty_html_formatter = [formatter for formatter in context._runner.formatters if isinstance(formatter, PrettyHTMLFormatter)][-1]
    # context._runner.formatters.remove(pretty_html_formatter)
    # pretty_html_formatter.close()
    pass

def after_all(context):
    pass