<script>
    import Button from "$lib/ExampleComponent.svelte";
</script>
<input class="chat-input" placeholder="Ask me anything"/>
<Button name="Send"/>

<style>
    .chat-input {
        width: calc(100% - 60px);
        border: 1px solid #49cc9a;
        border-radius: 10px;
        margin: 10px 0;
        padding: 10px;
    }
</style>