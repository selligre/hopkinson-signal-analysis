def action(d):
    print(f"window.action() called: {d.value}")
    d.add_data()
    return d
