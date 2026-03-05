<script lang="ts">
	import { resolve } from '$app/paths';
	let content = $state('');
	import site from './site.txt?raw';
	const { article } = $props();
	switch (article.link) {
		case 'site':
			content = site;
			break;

		default:
			content = '';
			break;
	}
</script>

<section class="py-20">
	<h1 class="mb-8 text-4xl font-bold text-purple-300">{article.title}</h1>

	<div class="space-y-6">
		<div class="border-l-2 border-purple-800 pl-6">
			<p class="text-lg text-purple-600">{article.header}</p>
		</div>
		{#each content.split('\\n') as paragraph}
			<p class="text-white">{paragraph}</p>
		{/each}
	</div>
	<div class="mt-15 border-l-2 border-purple-900 pl-6">
		<a class="text-lg text-purple-800" href={resolve('/blog')}> ← back</a>
	</div>
</section>
