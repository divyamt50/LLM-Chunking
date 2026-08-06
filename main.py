import gradio as gr

def analyze_text(text):
    # You can add your chunk doctor logic here later
    return "Hello from Chunk Doctor!"

# Build the layout using Blocks
with gr.Blocks() as demo:
    gr.Markdown("# Chunk Doctor")
    
    # Text input area corresponding to "Paste some text below"
    text_input = gr.Textbox(label="Paste some text below", lines=5)
    
    # Analyze button
    analyze_btn = gr.Button("Analyze Button")
    
    # Output section
    output_display = gr.Textbox(label="Output", value="")
    
    # Connect the button click to the function
    analyze_btn.click(
        fn=analyze_text, 
        inputs=text_input, 
        outputs=output_display
    )

# Automatically launch and open in your default browser
demo.launch(inbrowser=True)