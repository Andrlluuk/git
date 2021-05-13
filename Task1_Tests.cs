namespace TestingTasks
{
    using NUnit.Framework;

    [TestFixture]
    public partial class Tasks_Tests
    {
        // Не создавай новый Tasks, используй this.Tasks для тестирования

        [Test]
        public void BeSumOfAbs_WhenBothPositive()
        {
            var actual = this.Tasks.SumAbs(1, 2);
            Assert.AreEqual(3, actual);
        }

        [Test]
        public void BeSumOfAbs_WhenFirstNegative()
        {
            var actual = this.Tasks.SumAbs(-4, 2);
            Assert.AreEqual(6, actual);
        }

        [Test]
        public void BeSumOfAbs_WhenSecondNegative()
        {
            var actual = this.Tasks.SumAbs(4, -2);
            Assert.AreEqual(6, actual);
        }

        [Test]
        public void BeSumOfAbs_WhenBothNegative()
        {
            var actual = this.Tasks.SumAbs(-4, -2);
            Assert.AreEqual(actual, 6);
        }
    }
}