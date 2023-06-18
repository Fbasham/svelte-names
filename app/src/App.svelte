<script>
  import { onMount } from "svelte";
  let data = [];

  onMount(async () => {
    let res = await fetch("http://127.0.0.1:8000");
    data = (await res.json()).data;
  });

  let numNames = 1;
  $: names = Array.from({ length: numNames }, () => ({
    name: "",
    locked: false,
  }));
  let favourites = new Set();
  function getRandomName() {
    return data[(Math.random() * data.length) | 0];
  }
</script>

<h1>Svlete Names</h1>

<input type="number" min="1" max="5" bind:value={numNames} />
<button
  on:click={() =>
    (names = names.map((o) => (o.locked ? o : { ...o, ...getRandomName() })))}
  >random</button
>
{#each names as o, i}
  <div>
    <p>{o.name ?? "x"}</p>
    <button on:click={() => (names[i] = { ...names[i], locked: !o.locked })}
      >{o.locked ? "un" : ""}lock</button
    >
    <button on:click={() => (favourites = new Set([...favourites, o]))}
      >heart</button
    >
  </div>
{/each}

{#each [...favourites] as fav}
  {fav.name}
{/each}
