<script>
	import Skill from './skill.svelte';
</script>

<section class="py-20">
	<h1 class="mb-8 text-4xl font-bold text-purple-300">about</h1>

	<div class="space-y-6">
		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">Hello! I'm a programmer who loves making things.</p>
		</div>

		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">
				I am self taught in programming, and most recently have gotten into webdev (not react).
			</p>
		</div>

		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">
				My hobbies include <a
					href="https://youtube.com/shorts/H70yENQtb2w"
					class="text-purple-700"
					target="_blank"
				>
					lifting</a
				>
				and
				<a href="https://youtu.be/5QIY6ID1YlM" class="text-purple-700" target="_blank">Overwatch</a
				>, linked are my proudest acheivments in those passions.
			</p>
		</div>

		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">
				I am <a href="https://www.16personalities.com/" class="text-purple-700" target="_blank"
					>INTJ</a
				>, bearish on AI, and 22.5
				<a href="https://ffmicalculator.org/" class="text-purple-700" target="_blank">FFMI</a>.
			</p>
		</div>

		<h2 class="mt-12 mb-6 text-2xl font-bold text-purple-300">skills</h2>
		<div class="grid gap-3">
			<Skill skill="Python"></Skill>
			<Skill skill="C"></Skill>
			<Skill skill="Embedded Systems/Microcontrollers"></Skill>
			<Skill skill="Typescript"></Skill>
			<Skill skill="Machine Learning"></Skill>
			<Skill skill="SvelteKit"></Skill>
			<Skill skill="Math"></Skill>
			<Skill skill="Bench Press"></Skill>
			<Skill skill="Deadlift"></Skill>
		</div>
	</div>
</section>
