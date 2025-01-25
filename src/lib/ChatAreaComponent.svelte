<script>
    import ChatBarComponent from "./ChatBarComponent.svelte";
    import MessageBubbleComponent from "./MessageBubbleComponent.svelte";
</script>
<div>
    <div>
        <MessageBubbleComponent content="Hello, I am chat gpt I am chat gpt gpt gpt wrapper" type="ai"></MessageBubbleComponent>
        <MessageBubbleComponent content="Hello, I am chat gpt I am chat gpt gpt gpt wrapper" type="human"></MessageBubbleComponent>
    </div>
    <ChatBarComponent></ChatBarComponent>
</div>