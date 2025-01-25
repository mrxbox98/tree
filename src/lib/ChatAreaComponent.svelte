<script>
    import ChatBarComponent from "./ChatBarComponent.svelte";
    import MessageBubbleComponent from "./MessageBubbleComponent.svelte";
</script>
<div class="container">
    <div>
        <MessageBubbleComponent content="Hello, I am chat gpt I am chat gpt gpt gpt wrapper" type="ai"></MessageBubbleComponent>
        <MessageBubbleComponent content="Hello, I am chat gpt I am chat gpt gpt gpt wrapper" type="human"></MessageBubbleComponent>
    </div>
    <ChatBarComponent></ChatBarComponent>
</div>

<style>
    .container {
        width: 100%;
        margin: 10px;
    }
</style>