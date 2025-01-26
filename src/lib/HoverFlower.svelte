<script lang="ts">
    import { getAmazonPrices } from "$lib/client";

    export let flower = "";

    let mainel: HTMLElement;

    let info: any = undefined

    let loading = false;

    async function onHover() {
        loading = true

        console.log("Hovered");

        let amazonPrices = await getAmazonPrices(mainel.textContent+" seeds");

        console.log(amazonPrices);

        info = amazonPrices[0];

        console.log(info);

        box.style.top = `${mainel.getBoundingClientRect().top + mainel.getBoundingClientRect().height}px`;
        box.style.left = `${mainel.getBoundingClientRect().left}px`;
        box.style.display = "block";

        loading = false
    }

    let box: HTMLElement;
</script>

<code bind:this={mainel} class="{loading ? 'cursor-wait' : ''}" onmouseover={onHover}>{flower}</code>

<div bind:this={box} class="w-[200px] absolute hidden p-2 rounded-lg shadow-lg shadow-gray-500/50">
    {#if info}
        <img src={info.img} alt="" />
        <a href={info.link} target="_blank" class="hover:underline">{info.title}</a>
        <p class="font-semibold text-right">{info.price}</p>
    {/if}
</div>