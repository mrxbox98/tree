<script>
    import { getAmazonPrices } from "$lib/client";
    import HoverFlowerComponent from "./HoverFlowerComponent.svelte";

    export let content = "Error";
    export let type;
    export let color = "grey";
    export let float = "left"

    /**
     * @param {any} plants
     */
    async function loadPlants(plants) {
        /**
         * @type {any[]}
         */
        let hoverFlowerComponents = []

        for (let i = 0; i < plants.length; i++) {
            const plant = plants[i];
            const info = await getAmazonPrices(plant); 

            hoverFlowerComponents.push({
                component: HoverFlowerComponent,  
                props: {                          
                    flower: plant,        
                    info: info[0]    
                }      
            });
        }
        
        return hoverFlowerComponents;
    }

    async function scanMessage() {
        const plantMatches = content.match(/\*([^*]+)\*/g); // Find text between asterisks
        const plants = plantMatches ? plantMatches.map(plant => plant.replace(/\*/g, '')) : []; // Clean the asterisks
        let hoverFlowerComponents = await loadPlants(plants);
        console.log(hoverFlowerComponents)
    }

    $: if (type == "ai") scanMessage()

    if (type == "ai" || type == "waiting") {
        color = "#49cc9a";
    }
    else {
        color = "#cdd1d0";
        float = "right"
    }
</script>

<div class="flex">
    <div class="bubble {type}" style="background-color: {color};">
        {#if type !== "waiting"}
            <!-- Render content if type is not "waiting" -->
            {content}
        {:else}
            <img src="./loading.gif"/>
        {/if}
    </div>
</div>


<style>

    .bubble.ai {
        justify-content: flex-start; /* Align AI messages to the left */
    }

    .bubble.human {
        background-color: black;
        margin-left: auto;
    }

    .bubble {
        color: white;
        display: inline-block;; /* Keeps the bubble size fitting the text */
        padding: 10px; /* Adds space around the text inside the bubble */
        border-radius: 10px; /* Gives rounded corners */
        max-width: 100%; /* Prevents bubbles from overflowing */
        word-wrap: break-word; /* Breaks long words if necessary */
        max-width: 40%;
    }
</style>