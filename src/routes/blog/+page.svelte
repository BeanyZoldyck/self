<script lang="ts">
	import Blog from './blog.svelte';
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	interface Blg {
		title: string;
		link: string;
		desc: string;
	}
	let blogs: Array<Blg> = [
		{
			title: 'finally got around to making a personal site',
			desc: 'dont know how someone with an ego my size took this long',
			link: 'site'
		}
	];
</script>

<section class="py-20">
	<h1 class="mb-8 text-4xl font-bold text-purple-300">blog</h1>

	<div class="space-y-8">
		{#each blogs as blog}
			<Blog title={blog.title} desc={blog.desc} link={blog.link}></Blog>
		{/each}
	</div>
</section>
