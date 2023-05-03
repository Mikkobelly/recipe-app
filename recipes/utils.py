from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    # Create BytesIO buffer for the image
    buffer = BytesIO()

    # Create a plot with buffer obj as a file-like obj with png format 
    plt.savefig(buffer, format='png')

    # Set the cursor to the start of the stream
    buffer.seek(0)

    # Get the content of the file
    image_png = buffer.getvalue()

    # Encode the image_png (bytes-like obj)
    graph = base64.b64encode(image_png)

    # Decode to get the string as output
    graph = graph.decode('utf-8')

    # Free up the memory of buffer
    buffer.close()

    return graph

def get_chart(chart_type, data, **kwargs):
    # Switch plot backend to AGG (preferred solution to write PNG file)
    plt.switch_backend('AGG')

    # Specify the figure size
    fig = plt.figure(figsize=(8, 3))

    if (chart_type == '#1'):
        # set recipe name as x-axis and cooking time as y-axis for the bar chart
        plt.bar(data['name'], data['cooking_time'])
    elif (chart_type == '#2'):
        labels = kwargs.get('labels')
        plt.pie(data['cooking_time'], labels=labels)
    elif (chart_type == '#3'):
        plt.plot(data['name'], data['cooking_time'])
    else:
        print('Unknown chart type')

    # Specify layout details
    plt.tight_layout()

    chart = get_graph()
    return chart




