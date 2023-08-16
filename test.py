from FancyLogger import FancyLogger, FancyFormatter, Formats

logger = FancyLogger('Test', FancyFormatter(Formats.detailed))

logger.setLevel(0)

if __name__ == '__main__':
    logger.debug('This is a debug')
    logger.info('This is an info')
    logger.warning('This is a warning')

    try:
        int('Not an int')
    except Exception as e:
        logger.error(f'This is an error for {e}')

    try:
        int('Not an int either')
    except Exception as e:
        logger.exception(f'This is an error for {e}')

    logger.critical('IMPORTANT: THIS IS A CRITICAL MESSAGE')

    print('\n----- Testing Sub loggers -----\n')

    logger.sub('Sub 1').info('A sub to the parent')
    logger.sub('Sub 2').info('Another sub logger!')

    logger.sub('Sub 1').info('Previous one is still available!')
    logger.sub('Sub 1').sub('Sub in Sub').critical('EVEN SUBS CAN HAVE SUBS!')