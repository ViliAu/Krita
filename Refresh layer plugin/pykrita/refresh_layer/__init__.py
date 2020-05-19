from .refresh_layer import RefreshLayer

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = RefreshLayer(parent=app)
app.addExtension(extension)
