import pynecone as pc
import pynecone_supporter

class State(pc.State):
    color = "#aabbcc"

def contents():
    #print(pynecone_supporter.components.color_picker(on_change=State.set_color)) #<HexColorPicker onChange={(_e) => Event([E("state.set_color", {value:_e})])}/>
    #print(type(pynecone_supporter.components.color_picker(on_change=State.set_color))) #<class 'test.test.ColorPicker'>  
    return pc.box(
        pc.vstack(
            pc.text(State.color),
            pynecone_supporter.components.color_picker(on_change=lambda color: State.set_color(color)),
        ),
        background_color=State.color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(contents, route="/", title="Color picker")
app.compile()
