<script lang="ts">
    export let name = 'world';
    export let onclick = () => {}
</script>

<button on:click={onclick}>{name}</button>

<style>
    button {
        width: 55px;
        background-color: #8CC342;
        border: none;
        border-radius: 10px;
        margin: 10px 0;
        padding: 10px;
        color: white;
    }
</style>