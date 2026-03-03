<script>
	import { resolve } from '$app/paths';
</script>

<section class="py-20">
	<h1 class="mb-6 text-5xl font-bold text-purple-300 md:text-6xl">
		Hi, I'm <span class="text-purple-200">beanyzoldyck</span>
	</h1>
	<p class="mb-8 text-xl text-purple-400 md:text-2xl">I do things sometimes</p>
	<div class="flex gap-4">
		<a
			href={resolve('/about')}
			class="border border-purple-700 px-6 py-3 text-purple-300 transition-colors hover:border-purple-500"
		>
			[about]
		</a>
		<a
			href={resolve('/projects')}
			class="border border-purple-700 px-6 py-3 text-purple-300 transition-colors hover:border-purple-500"
		>
			[projects]
		</a>
		<a
			href={resolve('/contact')}
			class="border border-purple-700 px-6 py-3 text-purple-300 transition-colors hover:border-purple-500"
		>
			[contact]
		</a>
	</div>
</section>
