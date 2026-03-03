<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/hxh.png';
	import { resolve } from '$app/paths';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<header class="border-b border-purple-900 bg-black py-4">
	<nav class="mx-auto flex max-w-4xl items-center justify-between px-6">
		<a href={resolve('/')} class="text-white">~/home</a>
		<div class="flex gap-6">
			<a href={resolve('/about')} class="text-purple-300 hover:text-purple-200">about</a>
			<a href={resolve('/projects')} class="text-purple-300 hover:text-purple-200">projects</a>
			<a href={resolve('/contact')} class="text-purple-300 hover:text-purple-200">contact</a>
			<a href={resolve('/blog')} class="text-purple-300 hover:text-purple-200">blog</a>
		</div>
	</nav>
</header>

<main class="mx-auto min-h-screen max-w-4xl px-6 py-12">
	{@render children()}
</main>

<footer class="mt-12 border-t border-purple-900 py-6">
	<div class="mx-auto max-w-4xl px-6 text-sm text-purple-500">
		© {new Date().getFullYear()} — built with <span class="text-purple-400">SvelteKit</span>
	</div>
</footer>
