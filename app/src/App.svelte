<script>
  import { onMount } from "svelte";
  let data = [];
  let numNames = 0;
  let names = [];
  let favourites = [];

  onMount(async () => {
    let res = await fetch("http://127.0.0.1:8000");
    data = (await res.json()).data;
    if (localStorage.getItem("favourite-names")) {
      favourites = JSON.parse(localStorage.getItem("favourite-names"));
    }
  });

  function getRandomName() {
    return data[(Math.random() * data.length) | 0];
  }

  function handleChange(e) {
    let n = e.target.value;
    if (n == numNames) return;
    else if (n < numNames) names = names.slice(0, -1);
    else names = [...names, { name: "", locked: false }];
    numNames = n;
  }

  function addToFavourites(name) {
    favourites = [...new Set([...favourites, name])];
    localStorage.setItem("favourite-names", JSON.stringify(favourites));
  }

  function removeFromFavourites(name) {
    favourites = favourites.filter((e) => e !== name);
    localStorage.setItem("favourite-names", JSON.stringify(favourites));
  }
</script>

<h1>Svelte Names</h1>

<input type="number" min="1" max="5" on:change|preventDefault={handleChange} />
<button
  on:click={() =>
    (names = names.map((o) => (o.locked ? o : { ...o, ...getRandomName() })))}
  >random</button
>
{#each names as o, i}
  <div>
    <p>{o.name ?? "x"}</p>
    <button
      on:click={() => (names[i] = { ...names[i], locked: !o.locked })}
      disabled={!o.name}>{o.locked ? "un" : ""}lock</button
    >
    <button on:click={() => addToFavourites(o.name)} disabled={!o.name}
      >heart</button
    >
  </div>
{/each}

<h2>Favourites</h2>
<ul>
  {#each favourites as name}
    <li>
      <span>{name}</span><button on:click={() => removeFromFavourites(name)}
        >&times;</button
      >
    </li>
  {/each}
</ul>
