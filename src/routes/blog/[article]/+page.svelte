<script lang="ts">
	import { page } from '$app/state';
	import Article from './article.svelte';
	let link = $derived(page.params.article);
</script>

<Article title="site" header="took me long enough" {link}></Article>
