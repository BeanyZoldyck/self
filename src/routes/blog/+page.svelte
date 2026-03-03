<script lang="ts">
	import Blog from './blog.svelte';
	import s from './site.txt';
	interface Blg {
		title: string;
		link: string;
		desc: string;
	}
	let blogs: Array<Blg> = [
		{
			title: 'Finally got around to making a personal site',
			desc: "Can't imagine why it took so long with *my* ego",
			link: s
		}
	];
	let READ = false;
</script>

<section class="py-20">
	<h1 class="mb-8 text-4xl font-bold text-purple-300">projects</h1>

	<div class="space-y-8">
		{#each blogs as blog}
			<Blog title={blog.title} desc={blog.desc} link={blog.link}></Blog>
		{/each}
	</div>
</section>
