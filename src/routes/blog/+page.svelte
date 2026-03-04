<script lang="ts">
	import Article from './article.svelte';
	import Blog from './blog.svelte';
	import { page } from '$app/state';
	interface Blg {
		title: string;
		link: string;
		desc: string;
	}
	let blogs: Array<Blg> = [
		{
			title: 'Finally got around to making a personal site',
			desc: "Can't imagine why it took so long with *my* ego",
			link: 'site'
		}
	];

	let READ = page.url.searchParams.has('article');
	let link = page.url.searchParams.get('article');
</script>

{#if READ}
	<Article title="site" header="took me long enough" {link}></Article>
{:else}
	<section class="py-20">
		<h1 class="mb-8 text-4xl font-bold text-purple-300">blog</h1>

		<div class="space-y-8">
			{#each blogs as blog}
				<Blog title={blog.title} desc={blog.desc} link={blog.link}></Blog>
			{/each}
		</div>
	</section>
{/if}
