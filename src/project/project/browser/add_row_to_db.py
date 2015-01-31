from Products.Five.browser import BrowserView


class AddRowView(BrowserView):

    def __init__(self, context, request):
        super(AddRowView, self).__init__(context, request)

    def __call__(self):
        return 'ok'
