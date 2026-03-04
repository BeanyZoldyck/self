<script>
	import Skill from './skill.svelte';
  let skills = [

			"Programming (Python/C/Typescript)",
			"Embedded Systems/Microcontrollers",
			"Math (mostly Calculus)",
			"Machine Learning",
			"SvelteKit",
			"Lifing (Bench Press & Deadlift)",
  ]
</script>

<section class="py-20">
	<h1 class="mb-8 text-4xl font-bold text-purple-300">about</h1>

	<div class="space-y-6">
		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">i'm a programmer who loves making things.</p>
		</div>

		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">
				i am self taught in programming, first learning python in highscool and most recently have gotten into webdev (not react).
			</p>
		</div>

		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">
				my hobbies include <a
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
        my current tech stack is neovim (btw) + opencode on my laptop, and IDLE + vscode/opencode on my desktop. I usually deploy apps with sveltekit + firebase.
			</p>
		</div>
		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">
				i am <a href="https://www.16personalities.com/" class="text-purple-700" target="_blank"
					>INTJ</a
				>, relatively bearish on AI, 22.5
				<a href="https://ffmicalculator.org/" class="text-purple-700" target="_blank">FFMI</a>, and
				my favorite color is purple/black (if you couldn't tell).
			</p>
		</div>

		<h2 class="mt-12 mb-6 text-2xl font-bold text-purple-300">passions</h2>
		<div class="grid gap-3">
      {#each skills.sort(() => Math.random()-0.5) as skill}
        <Skill {skill}></Skill>

{/each}
		</div>
	</div>
</section>
