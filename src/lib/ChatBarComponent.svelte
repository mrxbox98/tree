<script>
    import Button from "$lib/ExampleComponent.svelte";
</script>
<input class="chat-input" placeholder="Ask me anything"/>
<Button name="Send"/>

<style>
    .chat-input {
        width: calc(100% - 60px);
    }
</style>