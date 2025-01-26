<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    function closeModal() {
        dispatch("close"); // Emit close event
    }
</script>

<div class="modal-backdrop" on:click={closeModal}>
    <div class="modal" on:click|stopPropagation>
        <div style="font-size: 30px;">Here are some useful tips</div>
        <br>
        <ul>
            <li><strong>/help</strong>: Open this help modal</li>
            <li><strong>/clear</strong>: Clear the chat</li>
            <li><strong>/conclude</strong>: What plant should I have</li>
            <br>
            <li>Type anything else to learn more about plants!</li>
        </ul>
        <button on:click={closeModal}>Close</button>
    </div>
</div>

<style>
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }

    .modal {
        background: white;
        border-radius: 10px;
        padding: 20px;
        max-width: 400px;
        width: 90%;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
    }

    .modal h2 {
        margin: 0 0 10px;
    }

    .modal ul {
        text-align: left;
        margin: 10px 0;
        padding-left: 20px;
    }

    .modal button {
        margin-top: 10px;
        background: #8cc342;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.2s ease-in-out;
    }

    .modal button:hover {
        background: #76a631;
    }
</style>
