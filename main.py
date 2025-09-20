from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    document.querySelector("#output").innerText = ""

    message = f""" Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

    Notes:
    {name} is currently {age} years old and studies at {school}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")