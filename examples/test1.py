import justpy as jp

def create_sidebar(wp, active_page=""):
    """Create a sidebar with navigation links."""
    sidebar = jp.Div(
        classes="w-1/4 bg-gray-800 h-screen text-white p-4 fixed", a=wp
    )
    jp.Div(text="Navigation", classes="text-xl font-bold mb-4", a=sidebar)

    links = {
        "Home": "/",
        "About": "/about",
        "Dictionary": "/dictionary",
    }

    for name, link in links.items():
        classes = "block p-2 hover:bg-gray-700 rounded"
        if active_page == name:
            classes += " bg-gray-700"
        jp.A(text=name, href=link, classes=classes, a=sidebar)

    return sidebar

@jp.SetRoute("/")
def home():
    wp = jp.WebPage()
    create_sidebar(wp, active_page="Home")
    div1 = jp.Div(classes="ml-1/4 p-4 text-center", a=wp)  # Adjust for sidebar
    jp.Div(text="Home", a=div1, classes="text-3xl p-5 bg-red-100")
    jp.Div(text="Welcome Home", a=div1, classes="text-lg m-2 mt-10 mb-10")
    return wp

@jp.SetRoute("/about")
def about():
    wp = jp.WebPage()
    create_sidebar(wp, active_page="About")
    div1 = jp.Div(classes="ml-1/4 p-4 text-center", a=wp)  # Adjust for sidebar
    jp.Div(text="About", a=div1, classes="text-3xl p-5 bg-red-100")
    jp.Div(text="Little About", a=div1, classes="text-lg m-2 mt-10 mb-10")
    jp.Div(
        text="This is a web app for instant dictionary",
        a=div1,
        classes="text-base m-2 mt-3 mb-3",
    )
    return wp

@jp.SetRoute("/dictionary")
def dictionary():
    wp = jp.WebPage()
    create_sidebar(wp, active_page="Dictionary")
    div1 = jp.Div(classes="ml-1/4 p-4 text-center", a=wp)  # Adjust for sidebar
    jp.Div(text="Dictionary", a=div1, classes="text-3xl p-5 bg-red-100")
    jp.Div(text="Instant Dictionary", a=div1, classes="text-lg m-2 mt-10 mb-10")

    # Search functionality
    form = jp.Div(classes="mt-5", a=div1)
    input_box = jp.Input(placeholder="Enter a word", a=form, classes="p-2 border")
    output = jp.Div(classes="mt-4", a=form)

    def search_word(self, msg):
        word = input_box.value.strip()
        if word:
            # Placeholder for dictionary search (can integrate with an API)
            output.text = f"Definition of '{word}': [Placeholder Definition]"
        else:
            output.text = "Please enter a word to search."

    jp.Button(text="Search", classes="bg-blue-500 text-white p-2 rounded", a=form, click=search_word)

    return wp

jp.justpy()
