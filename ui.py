import gradio as gr

from config import load_css
from profile_agent import Me


def create_demo():
    me = Me()

    def add_user_message(message, history):
        history = history or []
        message = (message or "").strip()
        if not message:
            return "", history
        return "", history + [{"role": "user", "content": message}]

    def add_assistant_message(history):
        history = history or []
        if not history or history[-1].get("role") != "user":
            return history
        user_message = history[-1]["content"]
        prior_history = history[:-1]
        reply = me.chat(user_message, prior_history)
        return history + [{"role": "assistant", "content": reply}]

    initial_history = [
        {
            "role": "assistant",
            "content": "Retrieval field online. Ask me about my background, work, or current engineering focus.",
        }
    ]

    with gr.Blocks(css=load_css(), title="Fey Career Archive") as demo:
        with gr.Column(elem_id="fey-app", elem_classes=["app-shell"]):
            gr.HTML(
                """
                <div class="system-strip" aria-hidden="true">
                    <span>FEY_CAREER_ARCHIVE v0.1.0</span>
                    <span>ACTIVE PROFILE NODE</span>
                </div>
                """
            )

            with gr.Column(elem_id="career-archive-panel", elem_classes=["archive-panel"]):
                gr.HTML(
                    """
                    <header class="archive-panel-header">
                        <span>Federica Recanatini / Software Engineer</span>
                    </header>
                    """
                )

                with gr.Column(elem_classes=["archive-panel-body"]):
                    gr.HTML(
                        """
                        <div class="terminal-intro" aria-hidden="true">
                            <span class="terminal-line terminal-line-process">&gt; retrieval field online.</span>
                            <span class="terminal-line terminal-line-ready">&gt; profile signal stabilized.</span>
                        </div>
                        """
                    )

                    chatbot = gr.Chatbot(
                        value=initial_history,
                        type="messages",
                        show_label=False,
                        height=460,
                        elem_id="career-chatbot",
                        elem_classes=["career-chatbot"],
                    )

                    with gr.Row(elem_classes=["prompt-row"]):
                        prompt = gr.Textbox(
                            label="> say",
                            show_label=False,
                            lines=1,
                            max_lines=4,
                            elem_id="career-input",
                        )
                        submit = gr.Button(
                            "send",
                            elem_id="career-submit",
                            elem_classes=["terminal-button"],
                        )

            gr.HTML(
                """
                <footer class="status-footer" aria-hidden="true">
                    <span>SYS: CAREER NODE_17</span>
                    <span>ARCHIVE INTEGRITY 100%</span>
                    <span>CONTACT CHANNEL: OPEN</span>
                </footer>
                """
            )

        submit_event = prompt.submit(
            add_user_message,
            [prompt, chatbot],
            [prompt, chatbot],
            queue=False,
        )
        submit_event.then(add_assistant_message, chatbot, chatbot)

        click_event = submit.click(
            add_user_message,
            [prompt, chatbot],
            [prompt, chatbot],
            queue=False,
        )
        click_event.then(add_assistant_message, chatbot, chatbot)

    return demo
