from custom_dmc_tasks import walker



def make(domain, task,
         task_kwargs=None,
         environment_kwargs=None,
         visualize_reward=False):

    if domain == 'walker':
        return walker.make(task,
                           task_kwargs=task_kwargs,
                           environment_kwargs=environment_kwargs,
                           visualize_reward=visualize_reward)
    else:
        raise f'{task} not found'
